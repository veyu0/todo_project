import React, { Component } from 'react';
import './App.css';
import axios from 'axios';
import UserList from './components/User.js'
import Project from './components/Project.js'
import ToDo from './components/ToDo.js'
import Menu from './components/Menu.js'
import Footer from './components/FooterPage.js'
import {BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom'
import LoginForm from './components/Auth.js'
import Cookies from 'universal-cookie';


const NotFound404 = ({ location }) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div> )
  }

class App extends React.Component {
    constructor(props) {
       super(props)
       this.state = {
           'users': [],
           'projects': [],
           'todos': [],
           'token': ''
       }
    }
    set_token(token) {
        const cookies = new Cookies() 
        cookies.set('token', token) 
        this.setState({'token': token}, ()=>this.load_data())
        }
    is_authenticated() {
        return this.state.token != ''
        }
    logout() { 
        this.set_token('')
        }
    get_token_from_storage() {
        const cookies = new Cookies() 
        const token = cookies.get('token') 
        this.setState({'token': token}, ()=>this.load_data())
        }
    
    get_token(username, password) { 
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password}) 
            .then(response => {
                this.set_token(response.data['token']) 
            }).catch(error => alert('Неверный логин или пароль'))
        }
    get_headers() { 
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()) {
            headers['Authorization'] = 'Token ' + this.state.token 
        }
        return headers 
    }

    load_data() {
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => { 
                this.setState({users: response.data})
            }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/projects/', {headers}) 
            .then(response => {
                this.setState({projects: response.data}) 
            }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/todos/', {headers}) 
            .then(response => {
                this.setState({todos: response.data}) 
            }).catch(error => console.log(error))
            this.setState({todos: []})
    }
    componentDidMount() {
        this.get_token_from_storage()
    }
    render() {
        return (
            <div className="App">
                <Menu />
                <BrowserRouter>
                    <nav>
                        <ul> 
                            <li>
                                <Link to='/users'>UserList</Link>
                            </li>
                            <li>
                            <Link to='/projects'>Projects</Link>
                            </li> 
                            <li>
                            <Link to='/todo'>ToDo</Link>
                            </li> 
                            <li>
                                {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/users' component={() => <UserList items={this.state.users} />} />
                        <Route exact path='/projects' component={() => <Project items={this.state.projects} />} />
                        <Route exact path='/todos' component={() => <ToDo items={this.state.todos} />} />
                        <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
                        <Redirect from='/users' to='/' />
                        <Route component={NotFound404} />
                    </Switch>
                </BrowserRouter>
                <Footer />
            </div>
        )
    }
    }

export default App;
