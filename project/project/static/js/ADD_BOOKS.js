function validateForm() {
    const id = document.getElementById("id").value;
    var title = document.getElementById("title").value;
    var author = document.getElementById("author").value;
    var category = document.getElementById("category").value;
    var description = document.getElementById("description").value;

    if (title === "") {
        alert("Name is required.");
        return false;
    }

    if (author === "") {
        alert("Author is required.");
        return false;
    } else if (!isValidAuthor(author)) {
        alert("Please enter a valid author name.");
        return false;
    }

    if (id === "") {
        alert("ID is required.");
        return false;
    }
    else if (!isValidId(id)) {
        alert("Please enter a valid ID.")
        return false;
    }

    if (category === "") {
        alert("Category is required.");
        return false;
    } else if (!isValidCategory(category)) {
        alert("Please enter a valid category.")
        return false;
    }
    
    if(description === ""){
        alert("Description is required.");
    }

    alert("Book added successfully.");
    return true;
}

function isValidAuthor(author) {
    var authorRegex = /^[a-zA-Z]+$/;
    return authorRegex.test(author);
}

function isValidId(id) {
    var idRegex = /^[0-9]+$/;
    return idRegex.test(id);
}

function isValidCategory(category) {
    var categoryRegex = /^[a-zA-Z ]+$/;
    return categoryRegex.test(category);
}


function addBook() {    
    if (validateForm()) {
        let id = document.getElementById("id").value;
        let title = document.getElementById("title").value;
        let author = document.getElementById("author").value;
        let category = document.getElementById("category").value;
        let description = document.getElementById("description").value;
        let imageUrl = document.getElementById("image-url").value; 

        let books = JSON.parse(localStorage.getItem('books')) || [];
        if (books.some(book => book.id === id)) {
            alert("Book ID already added.");
            return false; 
        }

        let bookDetails = {
            id: id,
            title: title,
            author: author,
            category: category,
            description: description,
            imageUrl: imageUrl, 
            available: true 
        };

        books.push(bookDetails);
        localStorage.setItem('books', JSON.stringify(books));

        console.log("Book added to local storage:", bookDetails); 

        displayBooks(); 
        return true;
    } else {
        return false;
    }
}


function displayBooks() {
    const bookList = document.getElementById("bookList");
    bookList.innerHTML = ""; 

    let books = JSON.parse(localStorage.getItem('books')) || [];
    books.forEach(book => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td><img src="${book.imageUrl}" alt="${book.title}" style="width:100px; height:auto;"></td>
            <td>${book.id}</td>
            <td>${book.title}</td>
            <td>${book.author}</td>
            <td>${book.category}</td>
            <td>${book.description}</td>
            <td>${book.available ? "Yes" : "No"}</td>
            <td><button onclick="editBook('${book.id}')">Edit</button></td>
            <td><button onclick="deleteBook('${book.id}')">Delete</button></td>
        `;
        bookList.appendChild(row);
    });
}

function editBook(bookId) {
    let books = JSON.parse(localStorage.getItem('books')) || [];
    const bookIndex = books.findIndex(book => book.id === bookId);
    if (bookIndex !== -1) {
        const book = books[bookIndex];
        const newName = prompt('Enter new name:', book.title);
        const newAuthor = prompt('Enter new author:', book.author);
        const newCategory = prompt('Enter new category:', book.category);
        const newDescription = prompt('Enter new description:', book.description);
        const isAvailable = confirm('Is the book available?');
        
        if (newName !== null && newAuthor !== null && newCategory !== null && newDescription !== null) {
            books[bookIndex] = {
                ...book,
                title: newName,
                author: newAuthor,
                category: newCategory,
                description: newDescription,
                available: isAvailable
            };

            localStorage.setItem('books', JSON.stringify(books));
            displayBooks();
        }
    } else {
        console.log('Book not found.');
    }
}

function deleteBook(bookId) {
    let books = JSON.parse(localStorage.getItem('books')) || [];
    const bookIndex = books.findIndex(book => book.id === bookId);
    if (bookIndex !== -1) {
        books.splice(bookIndex, 1);
        localStorage.setItem('books', JSON.stringify(books));
        displayBooks(); 
    } else {
        console.log('Book not found.');
    }
}

window.onload = displayBooks;
