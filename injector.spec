#include <frida-gum.h>
#include <dlfcn.h>
#include <iostream>

// This replaces the old 'cynject' logic
void inject_to_process(int pid, const char* dylib_path) {
    GumInterceptor *interceptor = gum_interceptor_obtain();
    // Use Frida's internal symbols or standard dlopen for rootless compatibility
    void* handle = dlopen(dylib_path, RTLD_NOW); 
    
    if (handle) {
        typedef void (*InitFunc)();
        InitFunc setup = (InitFunc)dlsym(handle, "CYServerSetup");
        if (setup) {
            setup(); // Start the Cycript REPL server in the target
            std::cout << "Successfully injected Cycript into PID: " << pid << std::endl;
        }
    } else {
        std::cerr << "Injection failed: " << dlerror() << std::endl;
    }
