let tab = [1,2,3];

tab.push("new item")

console.log(tab)

tab.unshift("początek")

console.log(tab)

console.log(tab.pop())

console.log(tab)

console.log(tab.shift())

console.log(tab)

//------------------

const kolory = ["red", "green", "blue"];

const nowList = kolory.map(k => `<li> ${k} </li>`)

console.log(nowList)

//-------------------

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