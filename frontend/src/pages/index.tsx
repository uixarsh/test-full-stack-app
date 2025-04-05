import React from "react";

import UserInterface from "../components/UserInterace";

const Home: React.FC = () => {
    return ( 
        <div>
            <UserInterface backendName="Flask Backend" />
        </div>
    );
}

export default Home;