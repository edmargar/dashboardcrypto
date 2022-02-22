import React, {useState, useEffect} from 'react'
import { DataGrid } from '@mui/x-data-grid';
import { ThemeProvider, createTheme  } from '@mui/material/styles';
import {api} from "../../api";


const columns = [
    {field: 'tipo', headerName: 'Operação', align:'center', headerAlign:'center'},
    {field: 'cryptomoeda', headerName: 'Moeda', align:'center', headerAlign:'center',
      valueGetter: (params) => {
      let result = [];
      result.push(params.row.cryptomoeda[0].nome);
      return result;
    }},
    {field: 'valor_operacao', headerName: 'Valor da operação', align:'center', headerAlign:'center'},
    {field: 'quantidade', headerName: 'Quantidade', align:'center', headerAlign:'center'},
    {field: 'exchange.nome', headerName: 'Exchange', width: 180, align:'center', headerAlign:'center',
      valueGetter: (params) => {
      let result = [];
      result.push(params.row.exchange[0].nome);
      return result;
    }},
    {field: 'data', headerName: 'Data da operação', width: 150, align:'center', headerAlign:'center'}
]
class DataTable extends Component{
        state = {
        negotiations: [],
    }

    async componentDidMount(){
        const response = await api.get('/finance/');
        this.setState({negotiations: response.data});
    }

    render(){
        return(
            <div style={{width: '90%', textAlign: 'center'}}>
                <h2>Negociações</h2>
                <div style={{ display: 'flex', height: '100%' }}>
                    <DataGrid sx={{
                                    boxShadow: 1,
                                    border: 2,

                                    borderColor: 'primary.light',
                                    '& .MuiDataGrid-cell:hover': {
                                      color: 'primary.main',
                                    },
                                  }}
                        autoHeight
                        rows={tableData}
                        columns={columns}
                        pageSize={20}
                    />
                </div>
            </div>
        );
    }
}

export default DataTable