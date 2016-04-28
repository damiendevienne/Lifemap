sudo -i -u postgres
psql -d tol
create index linesid on lines using way;
