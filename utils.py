#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :count_down.py
@说明        :
@时间        :2021/07/09 15:28:35
@作者        :张强
@版本        :1.0
'''
import time
from colorama import Fore, Back, Style


def count_down(num, sort):
    for i in range(num):
        if sort == 'D':
            print('                  ')
        else:
            print('')
        time.sleep(1)


def output_info(name, birthday, gender, weight, dad, mom):
    print('\033[94m       * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\033[0m')
    print('\033[94m       * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\033[0m')
    time.sleep(0.5)
    print('\033[94m       *                    '+Fore.RED+Style.RESET_ALL +
          'Father:   '+dad+'                                 *\033[0m')
    time.sleep(0.5)
    print('\033[94m       *                    Mother:   ' +
          mom+'                                 *\033[0m')
    time.sleep(0.5)
    print('\033[94m       *                    Brother:  张藤彧                                 *\033[0m')
    time.sleep(0.5)

    time.sleep(0.5)
    print('\033[94m       *  me:                                                                *\033[0m')
    time.sleep(0.5)
    print('\033[94m       *      name:  '+name +
          '              gender:  '+gender+'                        *\033[0m')
    time.sleep(0.5)
    print('\033[94m       *      birthday:  '+birthday +
          '   weight:  '+weight+'        *\033[0m')
    time.sleep(0.5)
    print('\033[94m       * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\033[0m')


# def output_info(name, birthday, gender, weight,dad,mom):

#     print('\033[94m       * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\033[0m')
#     time.sleep(0.5)
#     print('\033[94m       *                    Father:   '+dad+'                                 *\033[0m')
#     time.sleep(0.5)
#     print('\033[94m       *                    Mother:   '+mom+'                                 *\033[0m')
#     time.sleep(0.5)
#     print('\033[94m       *                    Brother:  张藤彧                                 *\033[0m')
#     time.sleep(0.5)
#     print('\033[94m       * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\033[0m')
#     time.sleep(0.5)
#     print('\033[94m       *  me:                                                                *\033[0m')
#     time.sleep(0.5)
#     print('\033[94m       *      name:  '+name+'              gender:  '+gender+'                        *\033[0m')
#     time.sleep(0.5)
#     print('\033[94m       *      birthday:  '+birthday+'   weight:  '+weight+'        *\033[0m')
#     time.sleep(0.5)
#     print('\033[94m       * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\033[0m')


def say_to_world(words):
    print('\033[94m       *                                                                     *\033[0m')
    time.sleep(0.5)
    print("\033[94m       *               "+"\033[91m" + words +
          "         I'm coming!!!\033[0m"+"                    *\033[0m")
    time.sleep(0.5)
    print('\033[94m       * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\033[0m')


def show(name, birthday, gender, words):
    time.sleep(0.5)
    print(Fore.CYAN+"          * * * * * * *     * * * * * * * *")
    time.sleep(0.5)
    print(Fore.CYAN+"        * * * * * * * * *  * * * * * * * * *")
    time.sleep(0.5)
    print(Fore.CYAN+"      * * * * * * * * * * * * * * * * * * * * *")
    time.sleep(0.5)
    print(Fore.CYAN+"     * * * * * * * * * * * * * * * * * * * * * *")
    time.sleep(0.5)
    print(Fore.CYAN+"    * *                                       * *")
    time.sleep(0.5)
    print(Fore.CYAN+"    * *                                       * *")
    time.sleep(0.5)
    print(Fore.CYAN+"    * *                  ", end='')
    print(Fore.RED+Style.BRIGHT+name, end='')
    print(Style.RESET_ALL+Fore.CYAN+"               * *")
    time.sleep(0.5)

    print(Style.RESET_ALL+Fore.CYAN+"    * *             ", end='')
    print(Fore.RED+Style.BRIGHT+birthday, end='')
    print(Style.RESET_ALL+Fore.CYAN+"        * *")
    time.sleep(0.5)

    print(Style.RESET_ALL+Fore.CYAN+"    * *                   ", end='')
    print(Fore.RED+Style.BRIGHT+gender, end='')
    print(Style.RESET_ALL+Fore.CYAN+"                 * *")
    time.sleep(0.5)

    print(Style.RESET_ALL+Fore.CYAN+"     * *                                     * * ")
    print(Fore.CYAN+"      * *                                   * * ")
    
    print(Fore.CYAN+"       * *            ",end='')
    print(Fore.RED+Style.BRIGHT+words, end='')
    print(Style.RESET_ALL+Fore.CYAN+"        * *")
    time.sleep(0.5)

    print(Fore.CYAN+"         * *          ",end='')
    print(Fore.RED+Style.BRIGHT+"I'm coming!!! ",end='')
    print(Style.RESET_ALL+Fore.CYAN+"    * *")
    time.sleep(0.5)
    print(Fore.CYAN+"           * *                         * * ")
    time.sleep(0.5)
    print(Fore.CYAN+"             * *                    * *")
    time.sleep(0.5)
    print(Fore.CYAN+"                * * * * * * * * * * * ")
    time.sleep(0.5)
    print(Fore.CYAN+"                      * * * * *")
    time.sleep(0.5)
    print(Fore.CYAN+"                         * *")
    time.sleep(0.5)
    print(Fore.CYAN+"                          *")


if __name__ == "__main__":
    show('张荣彧', '2021 年 7 月 12 日', 'Boy','Hello World!')
