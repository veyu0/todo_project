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
        </tr> )
}
const ToDo = ({items}) => {
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
            {items.map((item) => <ToDoItem item={item} />)}
        </table>
) }
export default ToDo;