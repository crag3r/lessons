class MyPerson {
    constructor(name) {
        this.name = name;
    }

    walk() {
        console.log("Im walking..")
    }
}

class Uczen extends MyPerson {
    constructor(name, school) {
        super(name);
        this.school = school;
    }
}

const janek = new Uczen("Jan", "Technikum");
console.log(janek)