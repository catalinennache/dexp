import math
n = input()

buffer = ""
s = 0

a = lambda x: math.floor(x*math.sqrt(2))
hiddenNumbers = list()
hiddenAdds = list()

lastHiddenNumber = -1

for x in range(int(n)):
    buffer += "+"+str(a(x))
    s+=a(x)
    if(x > 1):
        hiddenNumbers.append(x-)

print(buffer+"="+str(s))

"""
1+2+4+5+7+8+9+11+12+14+15+16+18+19+21+22+24+25+26+28+29+31+32+33+35+36+38+39+41+42+43+45+46+48+49+50+52+53+55+56+57+59+60+62+63+65+66+67+69+70+72+73+74+76+77+79+80+82+83+84+86+87+89+90+91+93+94+96+97+98+100+101+103+104+106+107+108+110+111+113+114+115+117+118+120+121+123+124+125+127+128+130+131+132+134+135+137+138+140+141+142+144+145+147+148+149+151+152+154+155+156+158+159+161+162+164+165+166+168+169+171+172+173+175+176+178+179+181+182+183+185+186+188+189+190+192+193+195+196+197+199+200+202+203+205+206+207+209+210+212+213+214+216+217+219+220+222+223+224+226+227+229+230+231+233+234+236+237+239+240+241+243+244+246+247+248+250+251+253+254+255+257+258+260+261+263+264+265+267+268+270+271+272+274+275+277+278+280+281=28044
3, 6, 13, 20, 23, 30, 37, 40, 47, 54,     |61| 64, 71, 78, 81, 88, 95, 102, 105, 112, 119, 126, 129, 136, 143,    |150|, 153, 160, 167, 170, 177, 184,   191, 194, 201, 204, 211, 218
+3, (+7, +7,) +3,(+7, +7,) +3,(+7, +7, +7),|+3|(+7, +7,) +3,(+7, +7, +7,)+3,(+7, +7, +7, +7,) +3, (+7, +7, +7, +7,) |+3|,  (+7,   +7,)  +3, (+7,  +7,  +7,)  +3, (+7), +3, +7, +7,

2 2 3 2 3 4 4 2 3 1



var a = {
    iteration:1,
    lastNumber: 1,
    isConsec:(x)=> x-1 == a.lastNumber,
    reset: ()=> {a.iteration = 1; a.lastNumber = 1},
    next: function(number){
        let consec = a.isConsec(number);
        a.lastNumber = number;
        if(consec){ a.iteration++;return false;}
        else {
            console.log(a.lastNumber -1, a.iteration)
            let response = a.iteration == 2;
            a.iteration = 1;
            return response;
        }
    }
}


buffer = ""
s = 0
a.reset();
f = (x) => Math.floor(x*Math.sqrt(2))
var hiddenNumbers = []
var hiddenAdds = []

lastHiddenNumber = -1

for(let x=0; x<400; x++){
    buffer += "+"+f(x)
    s+=f(x)
    if(x > 1){
        let resp = a.next(f(x));
        if(resp){
           hiddenNumbers.push(f(x)-1)
           if(hiddenNumbers.length > 1)
               hiddenAdds.push(hiddenNumbers[hiddenNumbers.length-1] - hiddenNumbers[hiddenNumbers.length-2])
               
        }
    }
}


hiddenAdds.join(" ").replaceAll("3"," ").split("   ").map(x=>x.replaceAll(" ","").length).join(" ")
"""
