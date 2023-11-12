import React, {useState, useEffect } from 'react'

function StockTable() {
    const [stockData, setStocData] = useState([]);

    useEffect (() => {
        // fetch data from the python backend 
        // and update state 
        // can use the fetch API or Axios if desired
    }, []);
    return (
        <div>
            <table>
                <thead>
                    <tr>
                        <th>Symbol</th>
                        <th>Company</th>
                        <th>Price</th>
                        {/*add more as required*/}
                    </tr>
                </thead>
                <tbody>
                    {stockData.map((stock) => (
                        <tr key={stock.symbol}>
                        <td>{stock.symbol}</td>
                        <td>{stock.companyName}</td>
                        <td>{stock.price}</td>
                        {/*add more fields if required*/}
            </tr>
            ))}        
            </tbody>
            </table>
        </div>
     );
}

export default StockTable;
