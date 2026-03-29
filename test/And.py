import frida
import sys

def on_message(message, data):
    print(f"[{message['type']}] -> {message['payload']}")

# 1. Connect to local emulator via ADB
device = frida.get_usb_device()

# 2. Spawn or attach to the target app
pid = device.spawn(["com.web4application.myapp"])
session = device.attach(pid)

# 3. Inject the Cycript-Frida bridge
script_source = """
    const lib = Module.load("/data/local/tmp/libcycript.so");
    const setup = new NativeFunction(lib.getExportByName("CYServerSetup"), 'void', []);
    setup();
    send("Cycript REPL server started in process.");
"""
script = session.create_script(script_source)
script.on('message', on_message)
script.load()

device.resume(pid)
print("Injection test complete. Check device logs.")
