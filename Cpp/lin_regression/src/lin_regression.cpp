#include <iostream>
#include <vector>
#include <random>
#include <cmath>

// Function to perform least squares regression
void leastSquaresRegression(const std::vector<double>& x, const std::vector<double>& y, double& slope, double& intercept)
{
    int n = x.size();
    double sumX = 0.0, sumY = 0.0, sumXY = 0.0, sumX2 = 0.0;

    for (int i = 0; i < n; ++i)
    {
        sumX += x[i];
        sumY += y[i];
        sumXY += x[i] * y[i];
        sumX2 += x[i] * x[i];
    }

    double meanX = sumX / n;
    double meanY = sumY / n;

    slope = (sumXY - n * meanX * meanY) / (sumX2 - n * meanX * meanX);
    intercept = meanY - slope * meanX;
}

int main()
{
    // Generate data points following a normal distribution curve
    int n = 100; // Number of data points
    double mean = 45.4453; // Mean of the normal distribution
    double stddev = 8.34; // Standard deviation of the normal distribution

    std::default_random_engine generator;
    std::normal_distribution<double> distribution(mean, stddev);

    std::vector<double> x(n);
    std::vector<double> y(n);

    for (int i = 0; i < n; ++i)
    {
        x[i] = i;
        y[i] = distribution(generator);
        std::cout << y[i] << ", ";
    }
    std::cout << std::endl;

    // Perform least squares regression
    double slope, intercept;
    leastSquaresRegression(x, y, slope, intercept);

    // Display the regression line equation
    std::cout << "Regression Line: y = " << slope << "x + " << intercept << std::endl;

    return 0;
}
