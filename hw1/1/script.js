// Store expenses in an array
let expenses = [];

// DOM elements
const expenseForm = document.getElementById('expenseForm');
const categoryInput = document.getElementById('category');
const amountInput = document.getElementById('amount');
const expensesList = document.getElementById('expensesList');
const totalExpenses = document.getElementById('totalExpenses');
const averageExpense = document.getElementById('averageExpense');
const topExpenses = document.getElementById('topExpenses');

// Add event listener for form submission
expenseForm.addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Get input values
    const category = categoryInput.value.trim();
    const amount = parseFloat(amountInput.value);
    
    // Add expense to array
    expenses.push({ category, amount });
    
    // Clear form
    categoryInput.value = '';
    amountInput.value = '';
    
    // Update UI
    updateExpensesList();
    updateSummary();
});

// Function to update expenses list
function updateExpensesList() {
    expensesList.innerHTML = '';
    
    expenses.forEach((expense, index) => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${expense.category}</td>
            <td>$${expense.amount.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</td>
            <td>
                <button class="delete-btn" onclick="deleteExpense(${index})">Delete</button>
            </td>
        `;
        expensesList.appendChild(row);
    });
}

// Function to delete expense
function deleteExpense(index) {
    expenses.splice(index, 1);
    updateExpensesList();
    updateSummary();
}

// Function to update summary
function updateSummary() {
    // Calculate total expenses
    const total = expenses.reduce((sum, expense) => sum + expense.amount, 0);
    totalExpenses.textContent = formatCurrency(total);
    
    // Calculate average daily expense
    const averageDaily = total / 30; // Assuming 30 days per month
    averageExpense.textContent = formatCurrency(averageDaily);
    
    // Find top 3 expenses
    const sortedExpenses = [...expenses].sort((a, b) => b.amount - a.amount);
    const top3 = sortedExpenses.slice(0, 3);
    
    topExpenses.innerHTML = top3.map(expense => 
        `<li>${expense.category}: ${formatCurrency(expense.amount)}</li>`
    ).join('');
}

// Helper function to format currency
function formatCurrency(amount) {
    return '$' + amount.toLocaleString('en-US', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });
}

// Add sample data (optional, can be removed)
function addSampleData() {
    const sampleData = [
        { category: 'Groceries', amount: 15000 },
        { category: 'Rent', amount: 40000 },
        { category: 'Transportation', amount: 5000 },
        { category: 'Entertainment', amount: 10000 },
        { category: 'Communication', amount: 2000 },
        { category: 'Gym', amount: 3000 }
    ];
    
    expenses = [...sampleData];
    updateExpensesList();
    updateSummary();
}

// Uncomment the line below to load sample data when the page loads
// addSampleData(); 