import React, { useState, useEffect } from 'react';
import axios from 'axios';
import CardComponent from './CardComponent';

interface User{
    id: number;
    username: string;
    email: string;
}

interface UserInterfaceProps{
    backendName: string;
}

const UserInterface: React.FC<UserInterfaceProps> = ({backendName}) => {

    const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:4000';
    const [users, setUsers] = useState<User[]>([]);
    const [newUser, setNewUser] = useState({id: '', name: '', email: ''})
    const [updatedUser, setUpdatedUser] = useState({id: '', name: '', email: ''})

    const backgroundColors: { [key: string]: string } = {
        flask: 'bg-blue-500',
    };

    const buttonColors: { [key: string]: string } = {
        flask: 'bg-blue-700 hover:bg-blue-600',
    };

    const bgColor = backgroundColors[backendName as keyof typeof backgroundColors] || 'bg-gray-200';
    const btnColor = buttonColors[backendName as keyof typeof buttonColors] || 'bg-gray-500 hover:bg-gray-600';


    // Fetch users from backend
    useEffect(() => {
        const fetchData = async () => {
            try{
                const response = await axios.get(`${apiUrl}/api/${backendName}/users`);
                setUsers(response.data.reverse());
            } catch (error) {
                console.error('Error fetching users:', error);
            }
        };
        fetchData();
    }, [backendName, apiUrl]);

    // Add user
    


    return (
        <div className={`user-interface ${bgColor} ${backendName} w-full max-w-md p-4 my-4 rounded shadow`}>
            <img src={`/${backendName}logo.svg`} alt={`${backendName} Logo`} className="w-20 h-20 mb-6 mx-auto" />
            <h2 className="text-xl font-bold text-center text-white mb-6">{`${backendName.charAt(0).toUpperCase() + backendName.slice(1)} Backend`}</h2>
        </div>
    );
}

export default UserInterface;
