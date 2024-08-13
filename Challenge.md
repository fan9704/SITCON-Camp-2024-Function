# Python 程式小挑戰

(Provided the English translation at the bottom.)

## 基礎語法 小挑戰


1. [Easy] 完成一個 n~m 數值加總的功能 
    - Ex: 1~100 => 5050
    - Hint:
        - 很像梯形公式
2. [Medium] 請製作 幾A幾B 遊戲 
    - Ex: 答案 1234 輸入 5213 輸出 1A2B
    - Hint:
        - 隨機產生 4位數數值 答案
        - 接收輸入
        - 
        - 一直重複判斷使用者輸入的正確性，其中有幾位數正確，幾位數錯誤
        - 輸出 幾位正確 [正確數量]A [錯誤數量] B
        - 答對成功遊戲結束

---

## 資料結構 小挑戰
1. [Easy] 找出數學和歷史都及格的學生，將這些學生的資料（一整個 dictionary）都存入 passed_students 這個 list 中，最後再印出 passed_students 的元素（elements）

學生資料（請複製到自己的 VSCode）：
```code=python
scoreList = [
    {"name": "Arnold", "Math": 87, "History": 92},
    {"name": "Beth", "Math": 45, "History": 78},
    {"name": "Chris", "Math": 66, "History": 54},
    {"name": "Diana", "Math": 88, "History": 64},
    {"name": "Evan", "Math": 72, "History": 93},
    {"name": "Fiona", "Math": 55, "History": 69},
    {"name": "George", "Math": 33, "History": 76},
    {"name": "Hannah", "Math": 47, "History": 83},
    {"name": "Ian", "Math": 99, "History": 57},
    {"name": "Jane", "Math": 78, "History": 91},
    {"name": "Kevin", "Math": 64, "History": 72},
    {"name": "Laura", "Math": 54, "History": 88},
    {"name": "Mike", "Math": 86, "History": 42},
    {"name": "Nina", "Math": 75, "History": 61},
    {"name": "Oscar", "Math": 23, "History": 90},
    {"name": "Paula", "Math": 67, "History": 56},
    {"name": "Quinn", "Math": 91, "History": 45},
    {"name": "Rachel", "Math": 48, "History": 67},
    {"name": "Steve", "Math": 77, "History": 38},
    {"name": "Tina", "Math": 59, "History": 84},
    {"name": "Uma", "Math": 93, "History": 47},
    {"name": "Vince", "Math": 34, "History": 86},
    {"name": "Wendy", "Math": 85, "History": 29},
    {"name": "Xander", "Math": 63, "History": 92},
    {"name": "Yara", "Math": 97, "History": 53},
    {"name": "Zane", "Math": 68, "History": 49},
    {"name": "Alex", "Math": 76, "History": 88},
    {"name": "Blake", "Math": 39, "History": 91},
    {"name": "Cindy", "Math": 81, "History": 34},
    {"name": "David", "Math": 92, "History": 65},
    {"name": "Ella", "Math": 60, "History": 79}
]
```

期待輸出：
![image](https://hackmd.io/_uploads/rk1OK78OR.png)
- Hint:
    - 分析一下資料的「組成是什麼」，例如是用什麼資料結構裝的，資料結構裡面的變數是什麼
    - 記得 list 有一個 method 可以計算長度
    - 在知道次數的情境下，迴圈建議使用...?
    - 使用 if 判斷式 : 
    - List 用 "index" 操控，Dictionary 用 "key" 操控
    - 用 .append() 或是 .insert() 把資料加入資料結構
    - 二維資料結構複習如下：
```code=python
scoreList = [{"name": "Alex", "Math": 20},{"name": "Diana", "History": 100}]

scoreList[1]
# 這樣就可以視為是 {"name": "Diana", "History": 100}
# （直接忽視前面的 {"name": "Alex", "Math": 20}）

scoreList[1]["name"]
# 這樣就可以視為是 "Diana"
# 其他我都不在乎，我眼中只有 Key 是 "name" 的資料


```
2. [Medium] 建立一個 JSON 檔案 當作資料庫儲存資料，請製作一個可以一直塞食物進冰箱的程式
    - Ex:
        - Input
            - Bread
            - Toast
            - Coco
            - exit
        - Output
            - [Bread,Toast,Coco]
    - Hint: 
        - 在專案資料夾下建立 foods.json 檔案內容是 []
        - Python 程式可以讀寫 foods.json 中的 []
        - 使用者可以輸入 食物名稱
        - 接者將食物 加入 json 中的 []
        - 持續進行直到使用者輸入 exit 離開並顯示冰箱現有的食物


---

## Function Module 小挑戰

1. [Easy] 製作一個能夠根據 使用者 輸入的名稱 輸出 Hello {使用者名稱} !
    - Ex: 輸入 Mary 輸出 Hello Mary!
2. [Hard] 製作一個計算機 Input: 2 + 1 Output 3 請避免使用者輸入非數值與非運算符號(請把 輸入/運算/轉換 各獨立成一個 Module)
    - Ex: 輸入 2 * 9 輸出 18 
    - Hint:
        - 使用者進入 main.py
        - 接收輸入 input.py
        - Split 輸入() input.py
        - 檢查可轉換成 數值/運算符號 compute.py 
        - 進行運算 compute.py
        - 輸出運算結果 main.py


## Translated by GPT4.0 :P
## Basic Syntax Challenges

1. [Easy] Implement a function to calculate the sum of numbers from n to m
    - Example: 1 to 100 => 5050
    - Hint:
        - It's similar to the trapezoid formula

2. [Medium] Create a Bulls and Cows game
    - Example: The answer is 1234, input is 2213, output is 2A2B
    - Hint:
        - Generate a random 4-digit number as the answer
        - Receive input from the user
        - Repeatedly check the correctness of the user's input, indicating how many digits are correct and in the correct position (A) and how many are correct but in the wrong position (B)
        - Output the number of correct digits as [Correct count]A[Incorrect count]B
        - If the guess is correct, end the game
## Data Structures Challenge
1. [Easy]Find students who passed both Math and History, store their data (the entire dictionary) in the passed_students list, and finally print the elements of passed_students.

Student data (please copy to your own VSCode):
```code=python
scoreList = [
    {"name": "Arnold", "Math": 87, "History": 92},
    {"name": "Beth", "Math": 45, "History": 78},
    {"name": "Chris", "Math": 66, "History": 54},
    {"name": "Diana", "Math": 88, "History": 64},
    {"name": "Evan", "Math": 72, "History": 93},
    {"name": "Fiona", "Math": 55, "History": 69},
    {"name": "George", "Math": 33, "History": 76},
    {"name": "Hannah", "Math": 47, "History": 83},
    {"name": "Ian", "Math": 99, "History": 57},
    {"name": "Jane", "Math": 78, "History": 91},
    {"name": "Kevin", "Math": 64, "History": 72},
    {"name": "Laura", "Math": 54, "History": 88},
    {"name": "Mike", "Math": 86, "History": 42},
    {"name": "Nina", "Math": 75, "History": 61},
    {"name": "Oscar", "Math": 23, "History": 90},
    {"name": "Paula", "Math": 67, "History": 56},
    {"name": "Quinn", "Math": 91, "History": 45},
    {"name": "Rachel", "Math": 48, "History": 67},
    {"name": "Steve", "Math": 77, "History": 38},
    {"name": "Tina", "Math": 59, "History": 84},
    {"name": "Uma", "Math": 93, "History": 47},
    {"name": "Vince", "Math": 34, "History": 86},
    {"name": "Wendy", "Math": 85, "History": 29},
    {"name": "Xander", "Math": 63, "History": 92},
    {"name": "Yara", "Math": 97, "History": 53},
    {"name": "Zane", "Math": 68, "History": 49},
    {"name": "Alex", "Math": 76, "History": 88},
    {"name": "Blake", "Math": 39, "History": 91},
    {"name": "Cindy", "Math": 81, "History": 34},
    {"name": "David", "Math": 92, "History": 65},
    {"name": "Ella", "Math": 60, "History": 79}
]
```

- Expected Output:
![image](https://hackmd.io/_uploads/rk1OK78OR.png)
- Hint:
    - Analyze the structure of the data, for example, what data structure is used and what variables are within the data structure
    - Remember that lists have a method to calculate their length
    - In situations where you know the number of iterations, use a loop
    - Use if statements to check conditions
    - Lists are accessed by "index", dictionaries are accessed by "key"
    - Use .append() or .insert() to add data to the data structure
    - Two-dimensional data structures can be reviewed as follows:
```code=python
scoreList = [{"name": "Alex", "Math": 20}, {"name": "Diana", "History": 100}]

scoreList[1]
# This will be considered as {"name": "Diana", "History": 100}
# (ignoring the previous {"name": "Alex", "Math": 20})

scoreList[1]["name"]
# This will be considered as "Diana"
# Ignoring all other keys, only the key "name" is of interest
```


2. [Medium] Create a JSON file to store data as a database, and make a program to keep adding food items to a refrigerator
- Example:
- Input

```code=c#
Bread
Toast
Coco
exit
```
- Output
```code=C#
[Bread,Toast,Coco]
```

- Hint:
    - Create a foods.json file in your project folder with content [] 
    - A Python program can read and write the [] in foods.json
    - The user can input food names
    - Add the food items to the JSON file's list
    - Continue this process until the user inputs exit, then display the current food items in the refrigerator

## Function Module Challenges
1. [Easy] Create a function that outputs "Hello {username}!" based on user input

- Example:
- Input: Mary
- Output: Hello Mary!

2. [Hard] Create a calculator

- Input: 2 + 1
- Output: 3

Avoid letting the user input non-numeric and non-operator symbols. (Separate input/operation/conversion into individual modules)

- Example:
    - Input: 2 * 9
    - Output: 18

- Hint:
    - The user enters through main.py
    - Input is received in input.py
    - Split the input in input.py
    - Check if it can be converted to
    - numeric/operator symbols in compute.py
    - Perform the calculation in compute.py
    - Output the result in main.py