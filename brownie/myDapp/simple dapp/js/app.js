

window.addEventListener('load', async function() {
  // Check if web3 is available in the browser
if (typeof window.ethereum !== 'undefined') {
    const web3 = new Web3(window.ethereum);
    try {
      // Request account access
      await window.ethereum.enable();
      // User has granted account access
      // You can now interact with the Ethereum network

      // Get the user's accounts
      const accounts = await web3.eth.getAccounts();
      // Use the first account as the default signer
      const signer = accounts[0];

      // Example: Send a transaction to a smart contract
      const contract = new web3.eth.Contract(ABI, CONTRACT_ADDRESS);
      await contract.methods.myMethod().send({ from: signer });

    } catch (error) {
      // User has denied account access
      console.error(error);
    }
  } else {
    // No web3 provider is available
    console.error('No web3 provider found. Consider installing MetaMask!');
  }

  
  if (window.ethereum) {
    const web3 = new Web3(ethereum);
    try {
      await ethereum.enable();
      const accounts = await web3.eth.getAccounts();
      console.log(accounts[0]);
    } catch (error) {
      console.error(error);
    }
  } else {
    console.error('Non-Ethereum browser detected. You should consider trying MetaMask!');
