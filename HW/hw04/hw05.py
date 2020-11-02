# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from HW.hw04.my_func import my_range, \
    my_reduce

even_day = [arg for arg in my_range(100,1001) if arg % 2 == 0]
print(my_reduce(lambda x,y: x*y, even_day))

#res reduce    = 11663575674444359823002008139390746528142707402328361705647495301216245827892256323421573853031635648105175857107321864360366071385039128549679496343675509640183219826717346573458260381851930244150425562315833417515264123698581740276921937117732298873364203269398167251131992557619396626253824845619285980851485012131859200089180731617159967796785692496658820266554970195579987101761437467345295469560091019643416890744175485355715583034412689664621367823158491721734017238669568797130683826947437814864890599291484009747561514288528353178159298856645624289518581586947168677504742711452824976368290519747367284033226821443792754573564848344600041433089899538479032717299413920051538113896509134682791976736868238046387230383008696853107977931851651379555533347652931008271572588724198961970056163028633888796670948358527288343719100865852117339478785474064397937004993302565523495403857150309972891503340949896943795594807214141508464167055846685872109706922589562538698747726222566785521882450614299594376824656706451033378744188256788426310583732611392640652066952551824890922829689995132928000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
#res my_reduce = 11663575674444359823002008139390746528142707402328361705647495301216245827892256323421573853031635648105175857107321864360366071385039128549679496343675509640183219826717346573458260381851930244150425562315833417515264123698581740276921937117732298873364203269398167251131992557619396626253824845619285980851485012131859200089180731617159967796785692496658820266554970195579987101761437467345295469560091019643416890744175485355715583034412689664621367823158491721734017238669568797130683826947437814864890599291484009747561514288528353178159298856645624289518581586947168677504742711452824976368290519747367284033226821443792754573564848344600041433089899538479032717299413920051538113896509134682791976736868238046387230383008696853107977931851651379555533347652931008271572588724198961970056163028633888796670948358527288343719100865852117339478785474064397937004993302565523495403857150309972891503340949896943795594807214141508464167055846685872109706922589562538698747726222566785521882450614299594376824656706451033378744188256788426310583732611392640652066952551824890922829689995132928000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
