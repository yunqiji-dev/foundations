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

