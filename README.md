# tasks_tbank

## Решение задач для поступления на стажировку в Т-Банк

#### задача 1

Костя подключен к мобильному оператору «Мобайл». Абонентская плата Кости составляет **﻿A**﻿ рублей в месяц. За эту стоимость Костя получает **﻿B**﻿ мегабайт интернет-трафика. Если Костя выйдет за лимит трафика, то каждый следующий мегабайт будет стоить ему **﻿C**﻿ рублей. Костя планирует потратить **﻿D**﻿ мегабайт интернет-трафика в следующий месяц. Помогите ему сосчитать, во сколько рублей ему обойдется интернет.

**Формат входных данных**

Вводится **﻿4**﻿ целых положительных числа **﻿A**,**B**,**C**,**D**(**1**≤**A**,**B**,**C**,**D**≤**1**0**0**)**﻿** — стоимость тарифа Кости, размер тарифа Кости, стоимость каждого лишнего мегабайта, размер интернет-трафика Кости в следующем месяце. Числа во входном файле разделены пробелами.

**Формат выходных данных**

Выведите одно натуральное число — суммарные расходы Кости на интернет.

**Замечание**

В первом примере Костя сначала оплатит пакет интернета, после чего потратит на **﻿5**﻿ мегабайт больше, чем разрешено по тарифу. Следовательно, за **﻿5**﻿ мегабайт он дополняет отдельно, получившаяся стоимость **﻿**100+12×5=160 рублей. Во втором примере Костя укладывается в тарифный план, поэтому платит только за него.
**100  10  12  15 - пример 1 входные данные
160 - на выходе
100  10  12  1 - пример 2 входные данные
100**

#### задача 2

Ваня принес на кухню рулет, который он хочет разделить с коллегами. Для этого он хочет разрезать рулет на **﻿N**﻿ равных частей. Разумеется, рулет можно резать только поперек. Соотвественно, Костя сделает **N**−**1**﻿ разрез ножом через равные промежутки.

По возвращению с кофе-брейка Ваня задумался — а можно ли было обойтись меньшим числом движений, будь нож Вани бесконечно длинным (иначе говоря, если он мог бы сделать сколько угодно разрезов за раз, если эти разрезы лежат на одной прямой)? Считается, что места для разрезов намечены заранее, и все разрезы делаются с ювелирной точностью.

Оказывается, что можно. Например, если Ваня хотел бы разделить рулет на **﻿4**﻿ части, он мог бы обойтись двумя разрезами — сначала он разделил бы рулет на две половинки, а потом совместил бы две половинки и разрезал обе пополам одновременно.

Вам дано число **﻿N**﻿, требуется сказать, каким минимальным числом разрезов можно обойтись.

**Формат входных данных**

Дано одно натуральное число **﻿N**(**1**≤**N**≤**2**×**10^9**)**﻿** — количество людей на кофе-брйке.

**Формат выходных данных**

Выведите одно число — минимальное число движений, которое придется сделать Косте.

**Замечание**

Чтобы разрезать рулет на **﻿6**﻿ частей, Ване сначала придется разрезать его на две равные части, после чего совместить две половинки и сделать два разреза. Чтобы разрезать рулет на **﻿5**﻿ частей, Ване понадобится разделить его в соотношении **﻿2**:**3**﻿, после чего совместить два рулета по левому краю и разрезать бОльший рулет на одинарные кусочки — меньший тоже разделится на одинарные.
**6 - пример 1 входные данные
3 - на выходе
5 - пример 2 входные данные
3 - на выходе**

#### задача 3

У Кати насыщенный день на работе. Ей надо передать n разных договоров коллегам. Все встре- чи происходят на разных этажах, а между этажами можно перемещаться только по лестничным пролетам — считается, что это улучшает физическую форму сотрудников. Прохождение каждого пролета занимает ровно **﻿1**﻿ минуту.

Сейчас Катя на парковочном этаже, планирует свой маршрут. Коллег можно посетить в любом порядке, но один из них покинет офис через **﻿t**﻿ минут. С парковочного этажа лестницы нет — только лифт, на котором можно подняться на любой этаж.

В итоге план Кати следующий:

1. Подняться на лифте на произвольный этаж. Считается, что лифт поднимается на любой этаж за **﻿0**﻿ минут.
2. Передать всем коллегам договоры, перемещаясь между этажами по лестнице. Считается, что договоры на этаже передаются мгновенно.
3. В первые **﻿t**﻿ минут передать договор тому коллеге, который планирует уйти.
4. Пройти минимальное количество лестничных пролетов.

Помогите Кате выполнить все пункты ее плана.

**Формат входных данных**

В первой строке вводятся целые положительные числа **﻿n**﻿ и **﻿t**﻿ **﻿**(2≤n,t≤100)﻿ — количество сотрудников и время, когда один из сотрудников покинет офис (в минутах). В следующей строке n чисел — номера этажей, на которых находятся сотрудники. Все числа различны и по абсолютной величине не превосходят 100. Номера этажей даны в порядке возрастания. В следующей строке записан номер сотрудника, который уйдет через t минут.

**Формат выходных данных**

Выведите одно число — минимально возможное число лестничных пролетов, которое понадобится пройти Кате.

**Замечание**

В первом примере времени достаточно, чтобы Катя поднялась по этажам по порядку. Во втором примере Кате понадобится подняться к уходящему сотруднику, а потом пройти всех остальных — например, в порядке **﻿{**1**,**2**,**3**,**4**,**6**}
пример 1, входные данные
5  5
1  4  9  16  25
2
на выходе
24
пример 2, входные данные
6  4
1  2  3  6  8  25
5
на выходе
31**

#### задача 4

У Кости есть бумажка, на которой написано **﻿**n**n**﻿ чисел. Также у него есть возможность не больше, чем **﻿**k**k**﻿ раз, взять любое число с бумажки, после чего закрасить одну из старых цифр, а на ее месте написать новую произвольную цифру. На какое максимальное значение Костя сможет увеличить сумму всех чисел на листочке?

**Формат входных данных**

В первой строке входного файла даны два целых числа **﻿n**,**k**﻿ — количество чисел на бумажке и ограничение на число операций. **(**1**≤**n**≤**1**000**,**1**≤**k**≤**10**^**4**)**﻿** . Во второй строке записано **﻿n**﻿ чисел **﻿**a — числа на бумажке **﻿**(1≤a≤10^9)﻿

**Формат выходных данных**

В выходной файл выведите одно число — максимальную разность между конечной и начальной суммой.

**Замечание**

В первом примере Костя может изменить две единицы на две девятки, в результате чего сумма чисел увеличится на **﻿16﻿**. Во втором примере Костя меняет число **﻿85﻿** на **﻿95﻿**. В третьем примере можно ничего не менять.
Обратите внимание, что ответ может превышать вместимость **﻿32﻿**-битного типа данных.
**пример 1, входные данные
5  2
1  2  1  3  5
на выходе
16
пример 2, входные данные
3  1
99  5  85
на выходе
10**
