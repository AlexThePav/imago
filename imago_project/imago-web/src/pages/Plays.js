import React from 'react';
import {PlayList} from '../plays';

export function Plays() {
    return (
        <div className="d-flex flex-row align-items-start flex-wrap mt-3 mx-3">
            <PlayList/>
        </div>
    )
}