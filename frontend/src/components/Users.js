import React from "react";

const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.email}</td>
            <td>{user.user_name}</td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <th>email</th>
            <th>user_name</th>
            <th>first_name</th>
            <th>last_name</th>
            {users.map(
                (user_map)=><UserItem user = {user_map} />
            )}
        </table>
    )
}

export default UserList