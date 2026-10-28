const partners = [
    { name: "Acme Corp", city: "Mumbai", creditLimit: 200000 },
    { name: "Blue Ridge Ltd", city: "Pune", creditLimit: 800000 },
    { name: "Sunrise Tech", city: "Delhi", creditLimit: 970089 },
    { name: "Green Foods", city: "Mumbai", creditLimit: 1289340 },
    { name: "Orbit Systems", city: "Ahmedabad", creditLimit: 278340 },
    { name: "Silver Line", city: "Pune", creditLimit: 280384 }
];

const tableBody = document.getElementById("partner-rows");

for (const partner of partners) {
    const row = document.createElement("tr");

    for (const value of [
        partner.name,
        partner.city,
        partner.creditLimit
    ]) {
        const cell = document.createElement("td");
        cell.textContent = value;
        row.appendChild(cell);
    }

            const actionCell = document.createElement("td");
        const deleteButton = document.createElement("button");

        deleteButton.type = "button";
        deleteButton.textContent = "Delete";

        deleteButton.addEventListener("click", () => {
            const index = partners.indexOf(partner);

            if (index !== -1) {
                partners.splice(index, 1);
            }

            searchInput.dispatchEvent(new Event("input"));
        });

        actionCell.appendChild(deleteButton);
        row.appendChild(actionCell);

    tableBody.appendChild(row);
}

const tableBody = document.getElementById("partner-rows");
const searchInput = document.getElementById("search");

const renderTable = (items) => {
    tableBody.replaceChildren();

    for (const partner of items) {
        const row = document.createElement("tr");

        for (const value of [
            partner.name,
            partner.city,
            partner.creditLimit
        ]) {
            const cell = document.createElement("td");
            cell.textContent = value;
            row.appendChild(cell);
        }

        tableBody.appendChild(row);
    }
};

renderTable(partners);

searchInput.addEventListener("input", () => {
    const searchText = searchInput.value.trim().toLowerCase();

    const matches = partners.filter((partner) => {
        return partner.name.toLowerCase().includes(searchText);
    });

    renderTable(matches);
});

const partnerForm = document.getElementById("partner-form");

partnerForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const name = document.getElementById("partner-name").value.trim();
    const city = document.getElementById("partner-city").value.trim();
    const creditLimit = Number(
        document.getElementById("partner-credit").value
    );

    if (!name || !city) {
        alert("Please enter a name and city.");
        return;
    }

    partners.push({
        name: name,
        city: city,
        creditLimit: creditLimit
    });

    partnerForm.reset();
    searchInput.value = "";
    searchInput.dispatchEvent(new Event("input"));
});