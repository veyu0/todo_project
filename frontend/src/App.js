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

    createProject(name, users) {
        const headers = this.get_headers()
        const data = {name: name, users: users} 
        axios.post(`http://127.0.0.1:8000/api/projects/`, data, {headers: headers})
            .then(response => {
                let new_project = response.data
                const users = this.state.users.filter((item) => item.id === new_project.users)[0] 
            new_project.users = users
            this.setState({projects: [...this.state.projects, new_project]}) 
        }).catch(error => console.log(error))}

    createToDo(name, user) {
        const headers = this.get_headers()
        const data = {name: name, user: user} 
        axios.post(`http://127.0.0.1:8000/api/todos/`, data, {headers: headers})
            .then(response => {
                let new_todo = response.data
                const user = this.state.user.filter((item) => item.id === new_todo.user)[0] 
            new_todo.user = user
            this.setState({todos: [...this.state.todos, new_todo]}) 
        }).catch(error => console.log(error))}

    deleteProject(id) {
        const headers = this.get_headers() 
        axios.delete(`http://127.0.0.1:8000/api/projects/${id}`, {headers: headers})
            .then(response => {
                this.setState({books: this.state.projects.filter((item)=>item.id !== id)})
        }).catch(error => console.log(error))
    }

    deleteToDo(id) {
        const headers = this.get_headers() 
        axios.delete(`http://127.0.0.1:8000/api/todos/${id}`, {headers: headers})
            .then(response => {
                this.setState({books: this.state.todos.filter((item)=>item.id !== id)})
        }).catch(error => console.log(error))
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
                        <Route exact path='/projects/create' component={() => <ProjectForm users={this.state.users} createProject={(name, users) => this.createProject(name, users)} />} />
                        <Route exact path='/todos/create' component={() => <ToDoForm user={this.state.user} createToDo={(name, user) => this.createToDo(name, user)}/>} />
                        <Route exact path='/projects' component={() => <Project items={this.state.projects} deleteProject={(id)=>this.deleteProject(id)}/>} />
                        <Route exact path='/todos' component={() => <ToDo items={this.state.todos} deleteToDo={(id)=>this.deleteToDo(id)}/>} />
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
