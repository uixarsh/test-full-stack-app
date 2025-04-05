import React from 'react';

interface Card{
    id: number;
    username: string;
    email: string;
}

const CardComponent: React.FC<{card : Card}> = ({card}) => {
    return (
        <div className="card">
            <h1>{card.username}</h1>
            <p>{card.email}</p>
        </div>
    )
};

export default CardComponent;
