
-- create ‘listenning’ socket 
local socket = require("socket")
local udp = socket.udp()
udp:settimeout(1)
udp:setsockname("*", 0)

-- get list of all devices on the lan 
local devices = {}
local ip, port = udp:getsockname()
for i=10,200 do
    local data, err = udp:receivefrom(255)
    if data ~= nil then
        local info = string.match(data, "([^:]+):(%d+)$")
        devices[info] = info
    end
    udp:sendto(i .. ":" .. port, ip, 53)
end

-- print out list of all devices on the lan
print(" Devices on lan")
for k, v in pairs(devices) do
    print("    " .. v)
end