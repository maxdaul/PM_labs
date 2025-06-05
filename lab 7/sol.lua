function createFib(st1, st2)
    n1 = st1
    n2 = st2
    return function()
        ans = n1 + n2
        n1 = n2
        n2 = ans
        return ans

    end
end
fibA = createFib(1, 1)
print(fibA())
print(fibA())
print(fibA())
print(fibA(), "\n")

fibB = createFib(0, 2)
print(fibB())
print(fibB())
print(fibB())
print(fibB(), "\n")

function createRandom()
    arr = {}
    return function()
        if #arr == 11 then
            return false
        end
        while true do
            ans = math.random(0, 10)
            if not find(arr, ans) then
                table.insert(arr, ans)
                return ans
            end
        end
    end

end

function find(arr, val)
    for _, i in ipairs(arr) do
        if val == i then
            return true
        end
    end
    return false
end

rnd = createRandom()
for i = 1, 14 do
    print(i.. "й вызов:", rnd())
end
