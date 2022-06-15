import React, { Component } from 'react';
import './App.css';
import axios from 'axios';
import UserList from './components/User.js'
import Project from './components/Project.js'
import ToDo from './components/ToDo.js'
import {BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom'

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
           'todo': []
       }
    }
    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/user')
            .then(response => {
                const users = response.data
                    this.setState(
                        {
                            'users': users
                        }
                    )
            }).catch(error => console.log(error))
        }
    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/project')
            .then(response => {
                const projects = response.data
                    this.setState(
                        {
                            'projects': projects
                        }
                    )
                }).catch(error => console.log(error))
            }
    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/todo')
            .then(response => {
                const todo = response.data
                    this.setState(
                        {
                            'todo': todo
                        }
                    )
                }).catch(error => console.log(error))
            }
    render() {
        return (
            <div className="App">
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
                </ul>
            </nav>
            <Switch>
                <Route exact path='/users' component={() => <UserList items={this.state.users} />} />
                <Route exact path='/projects' component={() => <Project items={this.state.projects} />} />
                <Route exact path='/todo' component={() => <ToDo items={this.state.todo} />} />
                <Redirect from='/users' to='/' />
                <Route component={NotFound404} />
            </Switch>
        </BrowserRouter>
      </div>
        )
    }
    }

export default App;
