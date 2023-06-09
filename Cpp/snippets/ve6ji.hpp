//-------------------------------------------
// VE6JI_HPP
//-------------------------------------------
#ifndef VE6JI_HPP
#define VE6JI_HPP
	// -- Debug Status --//
    #define debug_status true
    // Macro to print variable details
    #if debug_status
    #define D(x, y)                                                            \
        std::cout << x << "\t"                                                 \
            << "\033[;33m" << y << "\t\033[0m"                                 \
            << " in function [" << __PRETTY_FUNCTION__ << "] line {"           \
            << __LINE__ << "} of"                                              \
            << "[ " << __FILE__ << "]\t@ " << __TIME__ << " on " << __DATE__   \
            << std ::endl;
    #else
    #define D(...)
    #endif
	#define Yo "\033[;33m"
    #define Yc "\033[0m"
#endif // VE6JI_HPP