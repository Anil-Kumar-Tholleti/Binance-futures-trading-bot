const form = document.getElementById('orderForm');
const type = document.getElementById('type');
const extraFields = document.getElementById('extraFields');
const output = document.getElementById('output');

type.addEventListener('change', () => {
  extraFields.innerHTML = '';
  if (type.value === 'LIMIT') {
    extraFields.innerHTML += `
      <label>Limit Price:</label>
      <input type="number" id="limitPrice" step="0.01" required />
    `;
  }
  if (type.value === 'STOP') {
    extraFields.innerHTML += `
      <label>Stop Price:</label>
      <input type="number" id="stopPrice" step="0.01" required />
    `;
  }
});

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const symbol = document.getElementById('symbol').value;
  const side = document.getElementById('side').value;
  const orderType = type.value;
  const quantity = parseFloat(document.getElementById('quantity').value);

  const extra = {};
  if (orderType === 'LIMIT') {
    extra.limitPrice = parseFloat(document.getElementById('limitPrice').value);
  }
  if (orderType === 'STOP') {
    extra.stopPrice = parseFloat(document.getElementById('stopPrice').value);
  }

  // Simulate output
  output.innerHTML = `
    🧾 Placing ${side} ${orderType} order for ${quantity} ${symbol}
    ${extra.limitPrice ? `<br>Limit Price: ${extra.limitPrice}` : ''}
    ${extra.stopPrice ? `<br>Stop Price: ${extra.stopPrice}` : ''}
  `;
});
