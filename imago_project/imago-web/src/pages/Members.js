import React from 'react';
import { Route, Switch } from 'react-router-dom';

import {MemberList, MemberDetail} from '../members';

export function Members() {
    
    return (
        <div className="d-flex flex-row align-items-start flex-wrap mt-3">
            <Switch>
                <Route path="/members" exact component={MemberList}/>
                <Route path="/members/:slug" exact component={MemberDetail}/>
            </Switch>
        </div>
    )
}