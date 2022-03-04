import './Sidebar.css'
import logo from '../../assets/logo.png';

const Sidebar = ({sidebarOpen, closeSidebar}) => {
    return(
        <div className={sidebarOpen ? "sidebar-responsive": ""} id="sidebar">
            <div className="sidebar__tutle">
                <div className="sidebar__img">
                    <img src={logo} alt="logo"/>
                    <h1>Controle de investimentos</h1>
                </div>
                <i onClick={() => closeSidebar()}
                   className="fa fa-times"
                   id="sidebarIcon"
                   aria-hidden="true"
                />
            </div>
            <div className="sidebar__menu">
                <div className="sidebar__link active_menu_link">
                    <i className="fa fa-minus-square"/>
                    <a href='#'>Home</a>
                </div>
                <h2>ADMIN</h2>
                <div className="sidebar__link">
                    <i className="fa fa-tachometer"/>
                    <a href='#'>Cadastros</a>
                </div>
                <div className="sidebar__link">
                    <i className="fa fa-tachometer"/>
                    <a href='#'>Negociações</a>
                </div>
                <div className="sidebar__link">
                    <i className="fa fa-tachometer"/>
                    <a href='#'>Coinmarketcap</a>
                </div>
            </div>
        </div>
    )
}

export default Sidebar;