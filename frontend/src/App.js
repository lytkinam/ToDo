import React from "react";
import './App.css';
import UserList from "./components/Users";
import FooterPage from "./components/Footer";
import MenuList from "./components/Menu";
import axios from 'axios';

class App extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            'users':[],
            'authors':[],
        }
    }
    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/user/')
        .then(response => {
            const users = response.data
            this.setState({
                'users':users
            })
        })
        .catch(error => console.log(error))
    }
    render() {
        return(
            <div>
                <MenuList />
                <UserList users={this.state.users}/>
                <FooterPage/>
            </div>
        )
    }
}

export default App;
