#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <cstring>
#include <ctime>
#include <unistd.h>

int main() {
    // Create a UDP socket
    int sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock == -1) {
        std::cerr << "Failed to create socket!" << std::endl;
        return 1;
    }

    // Configure the recipient's address
    sockaddr_in recipientAddr{};
    recipientAddr.sin_family = AF_INET;
    recipientAddr.sin_port = htons(8080);  // Port 8080
    if (inet_aton("35.192.74.88 ", &recipientAddr.sin_addr) == 0) {  // Replace with actual recipient IP address
        std::cerr << "Invalid recipient IP address!" << std::endl;
        close(sock);
        return 1;
    }

    // Get the current timestamp
    time_t currentTime = time(nullptr);
    std::string message = std::to_string(currentTime);
    std::cout << "Sending message: " << message << std::endl;

    // Send the message
    ssize_t bytesSent = sendto(sock, message.c_str(), message.length(), 0, (const sockaddr*)&recipientAddr, sizeof(recipientAddr));
    if (bytesSent == -1) {
        std::cerr << "Failed to send message!" << std::endl;
        close(sock);
        return 1;
    }

    // Close the socket
    close(sock);

    return 0;
}