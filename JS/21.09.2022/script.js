let tab = [1,2,3];

tab.push("new item")

console.log(tab)

tab.unshift("początek")

console.log(tab)

console.log(tab.pop())

console.log(tab)

console.log(tab.shift())

console.log(tab)

//------------------- map

const kolory = ["red", "green", "blue"];

const nowList = kolory.map(k => `<li> ${k} </li>`)

console.log(nowList)

//------------------- forEach

const pies = {
    imie: 'Bożydar',
    wiek: 17,
    doesObeys: true
}

for(let i in pies) {
    console.log(`${i} - ${pies[i]}`)
}

let nic = [1,2,true, "Tomek"]

nic.forEach(value => console.log(String(value)+"200"))

//------------------- for of

const cos = ["polski", "matma", "informatyka"]

for(let sb of cos) {
    console.log(sb)
}

//------------------- destructing

const eurocrem = {
    imie: "ememe",
    wiek: 15,
    moc: 300
}

const imiemie = eurocrem.imie

console.log(imiemie)

const {imie, wiek, moc} = eurocrem

let osoba = {name: "John", age:33}

let {age} = osoba

console.log(age)

let {name: aaa} = osoba

