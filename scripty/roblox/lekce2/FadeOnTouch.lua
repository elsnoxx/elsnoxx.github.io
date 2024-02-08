local platform = script.Parent
local dotyk = false

local function zmizeni()
    if not dotyk then
        dotyk = true
        for count = 1, 10 do
            platform.Transparency = count / 10
            wait(0.1)
        end
        platform.CanCollide = false
        wait(3)
        platform.CanCollide = true
        platform.Transparency = 0
        dotyk = false
    end
end

platform.Touched:Connect(Fade)