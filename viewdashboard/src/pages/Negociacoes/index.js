import React, { Component } from 'react'
import Rotas from "../../Rotas";
import api from '../../api';
import DataTable from "../../component/negociacoes/Datagrid";
import Exemplo from "../../component/negociacoes/Exemplo";

function Index() {
    return(
        <div className="GridNegociacoes">

            <Exemplo/>
        </div>
    )
}

export default Index