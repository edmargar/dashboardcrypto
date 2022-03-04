import React from "react"
import {useState} from 'react';
import Rotas from './Rotas'

import './App.css';

import Sidebar from './component/sidebar/Sidebar'

const App = () => {
    const [sidebarOpen, setSiderbarOpen] = useState(false);
    const openSidebar = () => {
        setSiderbarOpen(true);
    };
    const closeSidebar = () => {
        setSiderbarOpen(false);
    };

    return (
        <div className="container">
            <Sidebar sidebarOpen={sidebarOpen} closeSidebar={closeSidebar}/>
            <div>
                <Rotas/>
            </div>
        </div>
    );
}

export default App;
