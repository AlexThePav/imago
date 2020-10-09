import React from 'react';
import { Route, Switch } from 'react-router-dom';

import {PlayList, PlayDetail} from '../plays';

export function Plays() {

    return (
        <div className="d-flex flex-row align-items-start flex-wrap mt-3 mx-3">
            <Switch>
                <Route path="/plays" exact component={PlayList} />
                <Route path="/plays/:slug" exact component={PlayDetail} />
            </Switch>
        </div>
    );
}