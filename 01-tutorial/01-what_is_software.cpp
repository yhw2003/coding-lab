/*
从用户视角看程序：输入 -> 处理 -> 输出
*/

#include <iostream>
extern void name_handle(char *);

int main() {
    char name[50] {};
    // 获得数据 
    std::cout << "Enter your name: ";
    std::cin >> name;
    // 处理数据
    name_handle(name);
    // 输出数据
    std::cout << "Hello, " << name << std::endl;
}

void name_handle(char * name) {
    // 转化为大写
    for (int i = 0; i < 50; i++) {
        if (name[i] == '\0') {
            break;
        }
        if (name[i] >= 'a' && name[i] <= 'z') {
            name[i] -= 32;
        }
    }
}