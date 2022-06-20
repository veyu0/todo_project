import React from 'react'

const ToDoItem = ({item}) => {
    return (
        <tr>
            <td>{item.project.name}</td>
            <td>{item.text}</td>
            <td>{item.user.username}</td>
            <td>{item.created}</td>
            <td>{item.updated}</td>
            <td>{item.active}</td>
            <td><button onClick={()=>deleteToDo(item.id)} type='button'>Delete</button></td>
        </tr> )
}
const ToDo = ({items, deleteToDo}) => {
    return (
        <table> 
            <tr>
                <th>Project name</th>
                <th>Text</th>
                <th>Username</th>
                <th>Created</th>
                <th>Updated</th>
                <th>Active</th>
            </tr>
            {items.map((item) => <ToDoItem item={item} deleteToDo={deleteToDo}/>)}
        </table>
) }
export default ToDo;