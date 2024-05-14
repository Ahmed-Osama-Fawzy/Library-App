class Book {
    constructor(ID, Name, author, Category, Description, isAvailable, imageUrl) {
        this.ID = ID;
        this.Name = Name;
        this.author = author;
        this.Category = Category;
        this.Description = Description;
        this.isAvailable = isAvailable;
        this.imageUrl = imageUrl;
    }
}

const library = [
    new Book(1, "Book 1", "Author 1", "Category 1", "Description 1", true,"book6.jpg"),
    new Book(2, "Book 2", "Author 2", "Category 2", "Description 2", false,"book6.jpg"),
    new Book(3, "Book 3", "Author 3", "Category 3", "Description 3", false,"book6.jpg"),
    new Book(4, "Book 4", "Author 4", "Category 4", "Description 4", true ,"book6.jpg"),
    new Book(5, "Book 5", "Author 3", "Category 5", "Description 5", false,"book6.jpg"),
    new Book(6, "Book 6", "Author 6", "Category 6", "Description 6", true ,"book6.jpg"),
    new Book(7, "Book 7", "Author 7", "Category 7", "Description 7", true,"book6.jpg"),
    new Book(8, "Book 8", "Author 3", "Category 8", "Description 8", false,"book6.jpg"),
    new Book(9, "Book 9", "Author 9", "Category 9", "Description 9", true,"book6.jpg"),

];

const addedbooks = [];
function loadBooks() {
    const storedBooks = JSON.parse(localStorage.getItem('books'));
    if (storedBooks) {
        addedbooks.length = 0;
        storedBooks.forEach(book => addedbooks.push(book));
    }
    displayBooks();
}
function saveToLocalStorage() {
    localStorage.setItem('books', JSON.stringify(addedbooks));
}

window.onload = loadBooks;

function addBook() {
    var ID = document.getElementById("id").value;
    var Name = document.getElementById("bname").value;
    var author = document.getElementById("ba").value;
    var Category = document.getElementById("category").value;
    var Description = document.getElementById("des").value;
    var isAvailable = document.getElementById("available").checked;
    var imageUrl = document.getElementById("image-url").value;
    var book = new Book(ID, Name, author, Category, Description, isAvailable, imageUrl);
    book.isAvailable = isAvailable;
    addedbooks.push(book);
    displayBooks();
    saveToLocalStorage();

    if (isAvailable) {
        let availableBooks = JSON.parse(localStorage.getItem('availableBooks')) || [];
        availableBooks.push(book);
        localStorage.setItem('availableBooks', JSON.stringify(availableBooks));
    }
}

function editBook(bookId) {
    const book = addedbooks.find(book => book.ID === bookId);
    if (!book) {
        console.log('Book not found.');
        return;
    }

    const newName = prompt('Enter new name:', book.Name);
    const newAuthor = prompt('Enter new author:', book.author);
    const newCategory = prompt('Enter new category:', book.Category);
    const newDescription = prompt('Enter new description:', book.Description);
    const isAvailable = confirm('Is the book available?');

    if (newName !== null && newAuthor !== null && newCategory !== null && newDescription !== null) {
        book.Name = newName;
        book.author = newAuthor;
        book.Category = newCategory;
        book.Description = newDescription;
        book.isAvailable = isAvailable;

        displayBooks();
        saveToLocalStorage();
    }
}

function deleteBook(bookId) {
    const index = addedbooks.findIndex(book => book.ID === bookId);
    if (index !== -1) {
        addedbooks.splice(index, 1);
        displayBooks();
    } else {
        console.log('Book not found.');
    }
    saveToLocalStorage()
}



function displayBooks() {
    const bookList = document.getElementById("bookList");
    bookList.innerHTML = addedbooks.map(book => `
        <tr>
            <td><img src="${book.imageUrl}" alt="${book.Name}" style="width:100px; height:auto;"></td>
            <td>${book.ID}</td>
            <td>${book.Name}</td>
            <td>${book.author}</td>
            <td>${book.Category}</td>
            <td>${book.Description}</td>
            <td>${book.isAvailable ? "Yes" : "No"}</td>
            <td><button onclick="editBook('${book.ID}')">Edit</button></td>
            <td><button onclick="deleteBook('${book.ID}')">Delete</button></td>
        </tr>
    `).join("");
}

window.onload = loadBooks;