import { DataGrid } from '@mui/x-data-grid';
import React, {useState, useEffect} from 'react'

export default function Exemplo() {
    const [isLoaded,setIsLoaded] = useState(false);
    const [rowData,setRowData] = useState([]);
    useEffect(() => {
        const axios = require('axios').default;
        axios
            .get('http://localhost:8000/api/finance/')
            .then((response) => {
            setIsLoaded(true);
            console.log(response.data);
            setRowData(response.data);
            response.data.forEach(user => {
            });
        });
    }, []);

    const columns = [
        { field: 'id', headerName: 'ID', width: 10 },
        { field: 'tipo', headerName: 'Tipo', width: 170 },
        { field: 'valor_operacao', headerName: 'Valor operação', width: 70 },
        { field: 'quantidade', headerName: 'Quantidade', width: 100 },
        { field: 'data', headerName: 'Data', width: 100 },
    ];

    return(
        <div style={{ height: 400, width: '100%' }}>
            <div style={{ display: 'flex', height: '100%' }}>
                <div style={{ flexGrow: 1 }}>
                    <DataGrid
                        columns={columns}
                        rows={rowData}
                        id='id'
                    pageSize={15}
                />
            </div>
        </div>
</div>
);
}