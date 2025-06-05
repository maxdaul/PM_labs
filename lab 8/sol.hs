import Data.Time

divf :: Fractional a => a -> a -> a
divf a b = a / b

safeDiv :: (Fractional a, Show a, Eq a) => (a -> a -> a) -> a -> a -> String
safeDiv func a b
  | b == 0    = "Нельзя делить на 0"
  | otherwise = show a ++ " поделить на " ++ show b ++ " равно " ++ show (func a b)

data LogRecord = LogRecord {
    params :: [String],   
    result :: String,     
    date :: String        
} deriving Show

type Log = [LogRecord]

loggedDiv :: (Show a, Fractional a) => (a -> a -> a) -> a -> a -> Log -> IO (String, Log)
loggedDiv func a b log = do
    let res = show (func a b)
    time <- fmap show getCurrentTime 
    let record = LogRecord { 
            params = [show a, show b], 
            result = res,
            date = time
        }
    return (res, record : log)

main :: IO ()
main = do
    putStrLn (safeDiv divf 16 3)
    putStrLn (safeDiv divf 10 0)
    putStrLn (safeDiv divf 0 0)

    (result1, log1) <- loggedDiv divf 10 2 []
    putStrLn $ "Результат выполнения функции: " ++ result1
    putStrLn "Лог выполнения функции:"
    mapM_ print log1

    (result2, log2) <- loggedDiv divf 10 0 log1
    putStrLn $ "Результат выполнения функции: " ++ result2
    putStrLn "Лог выполнения функции:"
    mapM_ print log2
