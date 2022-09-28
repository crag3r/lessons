import { MyPerson } from "myperson.js"

class Uczen extends MyPerson {
    constructor(name, school) {
        super(name);
        this.school = school;
    }
}

const janek = new Uczen("Jan", "Technikum");
console.log(janek)
