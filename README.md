1.	Krijojme nje array liste e cila permban shkronja, numra dhe karaktere speciale dhe e quajme: karakteret
karakteret = list(string.ascii_letters + string.digits + "!@#$%^&*()")

2.	Hapi tjeter, krijojme klasen 
def gjenero_password_te_rendomte():
3.	Kerkojme nga perdoruesi se sa karaktere do te kete password i gjeneruar dhe me ane te while, nese numri i marre nga perdoruesi eshte me i vogel ose barabarte se zero atehere programi do kerkoje qe perdoruesi te provoj perseri!
length = int(input("Shkruaj sa karaktere deshiron te kete passwordi juaj: "))
4.	Me ane te metodes random.shuffle, perzijme ne menyre te rendomte karakteret ne arrayin e krijuar ne hapin e pare (karakteret)
random.shuffle(karakteret)
5.	Krijojme nje liste te thate te quajtur password te cilen do e mbushim me numra random te marre nga array i sapo perzier (karakteret)
password = []
6.	Duke filluar nga 0 deri ne numrin e marre nga perdoruesi, mbushim array e krijuar me lart duke ia bashkangjitur nje karakter random nga array lista (karakteret)
for i in range(length):
    password.append(random.choice(karakteret))
7.	Perseri, me ane te metodes random.shuffle perziejme ne menyre te rendomte passwordin e gjeneruar
random.shuffle(password)
8.	Ne fund te klases, printojme passwordin e gjeneruar final!
print("".join(password))
9.	Per fund, thirrim klasen e krijuar per gjenerim te passwordit random 
gjenero_password_te_rendomte()



Punoi: Art Ramiqi
