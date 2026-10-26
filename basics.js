const partners = [
    { name: "Acme Corp", city: "Mumbai", creditLimit: 200000 },
    { name: "Blue Ridge Ltd", city: "Pune", creditLimit: 800000 },
    { name: "Sunrise Tech", city: "Delhi", creditLimit: 970089 },
    { name: "Green Foods", city: "Mumbai", creditLimit: 1289340 },
    { name: "Orbit Systems", city: "Ahmedabad", creditLimit: 278340 },
    { name: "Silver Line", city: "Pune", creditLimit: 280384 }
];


function partnersInCity(partners, city) {
    return partners.filter(function (partner) {
        return partner.city === city;
    });
}

const mumbaiPartners = partnersInCity(partners, "Mumbai");

console.log("Mumbai partners:", mumbaiPartners);

console.log(partners);
console.log("First partner:", partners[0].name);
console.log("Total partners:", partners.length);

function allNames(partners) {
    return partners.map(function (partner) {
        return partner.name;
    });
}

const names = allNames(partners);

console.log("Partner names:", names);

let total = 0;

for (const partner of partners) {
    total += partner.creditLimit;
}

console.log("Total credit:", total);
