import {test} from 'node:test';
import assert from 'node:assert/strict';
import {newEntries} from './additions.mjs';
const base='### Crime\n- [Existing](https://example.org/data) - Crime data\n  - Years: 2000-2020\n';
test('ignores description edits and renames with the same URL',()=>assert.equal(newEntries(base,base.replace('Existing','Renamed').replace('Crime data','Updated crime data')).length,0));
test('detects a new dataset without alerting on commented drafts',()=>assert.deepEqual(newEntries(base,base+' - [New](https://example.org/new) - New data\n<!--\n- Test A\n-->').map(e=>e.title),['New']));
test('detects datasets nested under a collection',()=>assert.deepEqual(newEntries(base,base+'  - [Chicago](https://example.org/chicago) - City records\n').map(e=>e.title),['Chicago']));
test('ignores a newly linked sample paper',()=>assert.equal(newEntries(base,base+'  - Sample paper: [Paper](https://example.org/paper)\n').length,0));
