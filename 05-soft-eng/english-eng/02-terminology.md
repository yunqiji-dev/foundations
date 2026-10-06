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
