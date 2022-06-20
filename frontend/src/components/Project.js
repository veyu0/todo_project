import React from 'react'
import {Link} from 'react-router-dom'

const ProjectItem = ({item}) => {
    return (
        <tr>
            <td>{item.name}</td>
            <td>{item.link}</td>
            <td>{item.user.username}</td>
            <td><button onClick={()=>deleteProject(item.id)} type='button'>Delete</button></td>
        </tr> )
}
const Project = ({items, deleteProject}) => {
    return (
    <table> 
        <tr>
                <th>Name</th>
                <th>Link</th>
                <th>Username</th>
        </tr>
            {items.map((item) => <ProjectItem item={item} deleteProject={deleteProject}/>)}
        <Link to='/projects/create'>Create</Link>
    </table>
) }
export default Project;