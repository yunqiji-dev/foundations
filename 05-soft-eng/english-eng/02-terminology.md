# Terminology

## Go basics

| English | 中文 | Note |
|---|---|---|
| package | 包 | Every Go file belongs to a package; programs start in `main` |
| import | 导入 | Brings another package into the file |
| exported name | 导出名 | Only names starting with a capital letter are visible outside the package |
| function | 函数 | The type comes after the parameter name |
| parameter / argument | 形参 / 实参 | Parameter is in the definition; argument is what you pass in |
| multiple results | 多返回值 | A function can return more than one value |
| named return value | 命名返回值 | Named results act as variables declared at the top of the function |
| naked return | 裸返回 | A bare `return` that returns the named results |
| variable declaration | 变量声明 | Uses `var` |
| short variable declaration | 短变量声明 | Uses `:=`; only allowed inside functions |
| zero value | 零值 | Default for uninitialized variables: `0`, `false`, `""` |
| type conversion | 类型转换 | Must be explicit in Go, e.g. `float64(i)` |
| type inference | 类型推断 | The type is taken from the value on the right-hand side |
| constant | 常量 | Declared with `const`; cannot use `:=` |
| rune | 字符（码点） | Alias for `int32`; one Unicode code point |
| byte | 字节 | Alias for `uint8` |


## Flow control

| English                                     | 中文                   | Note                                                                              |
| ------------------------------------------- | -------------------- | --------------------------------------------------------------------------------- |
| for loop                                    | for 循环               | Go's only looping construct                                                       |
| init statement / condition / post statement | 初始化语句 / 条件表达式 / 后置语句 | The three parts of a `for`, separated by semicolons; init and post are optional   |
| while loop                                  | while 循环             | Go has no `while`; write `for condition { }`                                      |
| infinite loop                               | 死循环                  | `for { }` with no condition                                                       |
| if statement                                | if 语句                | No parentheses around the condition; braces are required                          |
| short statement                             | 简短语句                 | `if v := f(); v < 10 { }`; runs before the condition                              |
| scope                                       | 作用域                  | A variable declared in the short statement exists only until the end of the `if`  |
| else                                        | else 分支              | Variables from the short statement are also visible in the `else` blocks          |
| Newton's method                             | 牛顿迭代法                | Used in the exercise: repeat `z -= (z*z - x) / (2*z)` to approach the square root |
| switch statement                            | switch 语句            | Runs only the first matching case; no `break` needed                              |
| case / default                              | 分支 / 默认分支            | Cases need not be constants or integers                                           |
| evaluation order                            | 求值顺序                 | Cases are checked top to bottom and stop at the first match                       |
| switch with no condition                    | 无条件 switch           | Same as `switch true`; a clean way to write a long if-else chain                  |
| defer                                       | 延迟调用                 | Runs when the surrounding function returns; arguments are evaluated immediately   |
| LIFO (last in, first out)                   | 后进先出                 | Deferred calls are pushed onto a stack and run in reverse order                   |




## More types

| English | 中文 | Note |
|---|---|---|
| pointer | 指针 | Holds the memory address of a value; zero value is `nil` |
| address-of operator | 取地址运算符 | `&x` generates a pointer to `x` |
| dereference | 解引用 | `*p` reads or sets the value the pointer points to |
| pointer arithmetic | 指针运算 | Go has none, unlike C |
| struct | 结构体 | A collection of fields |
| field | 字段 | Accessed with a dot; `p.X` also works when `p` is a pointer to a struct |
| struct literal | 结构体字面量 | `Vertex{1, 2}` or `Vertex{X: 1}`; unnamed fields get their zero value |
| array | 数组 | Fixed length; the length is part of the type, so `[3]int` and `[4]int` differ |
| slice | 切片 | A dynamically-sized view into an array; stores no data itself |
| half-open range | 左闭右开区间 | `a[low:high]` includes `low` and excludes `high` |
| underlying array | 底层数组 | Changing a slice element changes the array, and every other slice sharing it |
| slice literal | 切片字面量 | `[]int{1, 2, 3}`; builds the array and a slice that references it |
| slice defaults | 切片默认边界 | Omitted bounds default to `0` and the length: `a[:]`, `a[:5]`, `a[2:]` |
| length / capacity | 长度 / 容量 | `len(s)` is the number of elements; `cap(s)` counts from the slice's first element to the end of the array |
| nil slice | nil 切片 | The zero value of a slice; length and capacity are 0 |
| make | make（内置函数） | `make([]int, 0, 5)` allocates a zeroed array and returns a slice of it |
| slices of slices | 二维切片 | A slice whose elements are slices |
| append | 追加 | Returns a new slice; grows into a bigger array when capacity runs out, so write `s = append(s, x)` |
| range | 遍历 | `for i, v := range s` gives the index and a copy of the element |
| blank identifier | 空白标识符 | `_` discards a value you do not need |
| map | 映射（哈希表） | Maps keys to values; a `nil` map cannot be written to, so create it with `make` |
| map literal | 映射字面量 | `map[string]int{"a": 1}`; keys are required |
| key / value | 键 / 值 | Insert `m[k] = v`, read `m[k]`, remove `delete(m, k)` |
| comma ok | 存在性检查 | `v, ok := m[k]`; `ok` is `false` when the key is absent |
| function value | 函数值 | Functions are values and can be passed as arguments or returned |



## Algorithms

| English | 中文 | Note |
|---|---|---|
| algorithm | 算法 | A clear sequence of steps that solves a problem |
| brute force | 暴力解法 | Try every possibility; usually nested loops; correct but often slow |
| time complexity | 时间复杂度 | How the number of steps grows as the input size n grows |
| space complexity | 空间复杂度 | How much extra memory grows with n; the input itself is not counted |
| Big O notation | 大 O 表示法 | Keeps only the fastest-growing term, e.g. `O(n)`, `O(n²)` |
| constant time | 常数时间 | `O(1)`: same cost no matter how large n is, e.g. a map lookup |
| linear time | 线性时间 | `O(n)`: one pass over the input |
| quadratic time | 平方时间 | `O(n²)`: nested loops over the input; too slow when n reaches 10⁵ |
| constraints | 约束条件 | The input limits on the problem page; tell you which complexity will pass |
| hash table | 哈希表 | Go's `map`; insert and look up in `O(1)` on average |
| space-time trade-off | 空间换时间 | Use extra memory, such as a map, to cut the running time |
| Time Limit Exceeded (TLE) | 超时 | LeetCode's result when a solution is too slow |
