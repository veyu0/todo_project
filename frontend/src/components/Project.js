import React from 'react'

const ProjectItem = ({item}) => {
    return (
        <tr>
            <td>{item.name}</td>
            <td>{item.link}</td>
            <td>{item.user.username}</td>
        </tr> )
}
const Project = ({items}) => {
    return (
    <table> 
        <tr>
                <th>Name</th>
                <th>Link</th>
                <th>Username</th>
        </tr>
            {items.map((item) => <ProjectItem item={item} />)}
    </table>
) }
export default Project;