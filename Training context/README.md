# A. Андрей и кислота

Ограничение времени 2 секунды  
Ограничение памяти 512Mb  
Ввод стандартный ввод или input.txt  
Вывод стандартный вывод или output.txt  

Андрей работает в секретной химической лаборатории, в которой производят опасную кислоту с удивительными свойствами. У Андрея есть n бесконечно больших резервуаров, расположенных в один ряд. Изначально в каждом резервуаре находится некоторое количество кислоты. Начальство Андрея требует, чтобы во всех резервуарах содержался одинаковый объем кислоты. К сожалению, разливающий аппарат несовершенен. За одну операцию он способен разлить по одному литру кислоты в каждый из первых k *(1 ≤ k ≤ n)* резервуаров. Обратите внимание, что для разных операций k могут быть разными. Поскольку кислота очень дорогая, Андрею не разрешается выливать кислоту из резервуаров. Андрей просит вас узнать, можно ли уравнять объемы кислоты в резервуарах, и, если это возможно, то посчитать минимальное количество операций, которое потребуется, чтобы этого достичь.

## Формат ввода
Первая строка содержит число n *(1 ≤ n ≤ 100000)* — количество резервуаров. Во второй строке содержатся n целых чисел ai *(1 ≤ ai ≤ 109)*, где ai означает исходный объём кислоты в i-м резервуаре в литрах.
## Формат вывода
Если объемы кислоты в резервуарах можно уравнять, выведите минимальное количество операций, необходимых для этого.
Если это невозможно, выведите «-1».

### Пример 1

Ввод  
2  
1 2  
Вывод  
1  

### Пример 2

Ввод  
5  
1 1 5 5 5  

Вывод  
4  

### Пример 3

Ввод  
3  
3 2 1  

Вывод  
-1  


# B. Посадка в самолет

Ограничение времени	2 секунды  
Ограничение памяти	512Mb  
Ввод	стандартный ввод или input.txt  
Вывод	стандартный вывод или output.txt  


В самолете n рядов и по три кресла слева и справа в каждом ряду. Крайние кресла (A и F) находятся у окна, центральные (C и D) – у прохода. На регистрацию приходят группы из одного, двух или трех пассажиров. Они желают сидеть рядом, то есть на одном ряду и на одной стороне: левой или правой. Например, группа из двух пассажиров может сесть на кресла B и C, но не может сесть на кресла C и D, потому что они разделены проходом, а также не может сесть на кресла A и C, потому что тогда они окажутся не рядом. Кроме того, один из пассажиров каждой группы очень требовательный – он хочет сесть либо у окна, либо у прохода. Конечно же, каждая группа из пассажиров хочет занять места в ряду с как можно меньшим номером, ведь тогда они скорее выйдут из самолета после посадки. Для каждой группы пассажиров определите, есть ли места в самолете, подходящие для них.

## Формат ввода
Первая строка содержит число n *(1 ≤ n ≤ 100)* – количество рядов в самолете. Далее в n строках вводится изначальная рассадка в самолете по рядам (от первого до n-го), где символами . (точка) обозначены свободные места, символами # (решетка) обозначены занятые места, а символами _ (нижнее подчеркивание) обозначен проход между креслами C и D каждого ряда.
Следующая строка содержит число m *(1 ≤ m ≤ 100)* – количество групп пассажиров. Далее в m строках содержатся описания групп пассажиров. Формат описания такой: num side position, где num – количество пассажиров (число 1, 2 или 3), side – желаемая сторона самолета (строка left или right), position – желаемое место требовательного пассажира (строка aisle или window).

## Формат вывода
Если группа может сесть на места, удовлетворяющие ее требованиям, то выведите строку Passengers can take seats: и список их мест в формате *row letter*, упорядоченный по возрастанию буквы места. Затем выведите в n строках получившуюся рассадку в самолете, в формате, описанном выше, причем места, занятые текущей группой пассажиров, должны быть обозначены символом X.

Если группа не может найти места, удовлетворяющие ее требованиям, то выведите строку Cannot fulfill passengers requirements.
Ответ сравнивается с правильным посимвольно, поэтому ваше решение не должно выводить никаких лишних символов, в том числе лишних переводов строк или пробельных символов в концах строк. В конце каждой строки (включая последнюю) должен быть выведен символ перевода строки.

## Пример

Ввод
4  
...\_.#.  
.##\_...  
.#.\_.##  
...\_...  
7  
2 left aisle  
3 right window  
2 left window  
3 left aisle  
1 right window  
2 right window  
1 right window  

Вывод

Passengers can take seats: 1B 1C  
.XX\_.#.  
.##\_...  
.#.\_.##  
...\_...  
Passengers can take seats: 2D 2E 2F  
.##\_.#.  
.##\_XXX  
.#.\_.##  
...\_...  
Passengers can take seats: 4A 4B  
.##\_.#.  
.##\_###  
.#.\_.##  
XX.\_...  
Cannot fulfill passengers requirements  
Passengers can take seats: 1F  
.##\_.#X  
.##\_###  
.#.\_.##  
##.\_...  
Passengers can take seats: 4E 4F  
.##\_.##  
.##\_###  
.#.\_.##  
##.\_.XX  
Cannot fulfill passengers requirements 

# C. Расстояние

| Язык                    | Ограничение времени | Ограничение памяти | 	Ввод                          | Вывод                            |
| ----------------------- |:-------------------:| :----------------: | :-----------------------------:| :-------------------------------:|
| Все языки               | 2 секунды           | 512Mb              |                                |                                  |
| Python 3.7.3            | 4 секунды           | 512Mb              |                                |                                  |
| Python 3.7 (PyPy 7.3.3) | 4 секунды           | 512Mb              | стандартный ввод или input.txt | стандартный вывод или output.txt |
| Python 2.7              | 4 секунды           | 512Mb              |                                |                                  |
| PHP 7.3.5               | 4 секунды           | 512Mb              |                                |                                  |

Рассмотрим целочисленный массив a длины n. Назовём расстоянием от индекса i до множества индексов S величину *dist(i, S) = ∑j∈S ∣ai − aj∣*.

Зафиксируем целое число k. Рассмотрим функцию *f(i) = mindist(i, S)*, где минимум берётся по множествам S размера k, не содержащим индекс i. Определите значение f(i) для всех i от 1 до n.

## Формат ввода

В первой строке заданы два целых числа n и k *(2 ≤ n ≤ 300000, 1 ≤ k < n)*, описанные в условии. Во второй строке содержится n целых чисел ai *(1 ≤ ai ≤ 109)* — элементы массива a.

## Формат вывода

Выведите n целых чисел: значения f(i) для i=1, i=2 , …, i=n.

## Пример 1

Ввод:

4 2  
1 2 3 4  

Вывод:

3 2 2 3  

## Пример 2

Ввод:

5 3  
3 2 5 1 2  

Вывод:

4 2 8 4 2  

## Пример 3

Ввод:

6 2  
3 2 1 101 102 103  

Вывод:

3 2 3 3 2 3